/* vim: set sw=4 sts=4 : */

/*
 * Author David Bruno Cortarello <Nomius>. Redistribute under the terms of the
 * BSD-lite license. Bugs, suggests, nor projects: dcortarello@gmail.com
 *
 * Program: icmp_send
 * Version: 0.1
 *
 *
 * Copyright (c) 2005-2008, David B. Cortarello
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 *  * Redistributions of source code must retain the above copyright notice
 *    and the following disclaimer.
 *  * Redistributions in binary form must reproduce the above copyright notice
 *    and the following disclaimer in the documentation and/or other materials
 *    provided with the distribution.
 *  * Neither the name of Kwort nor the names of its contributors may be used
 *    to endorse or promote products derived from this software without
 *    specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/select.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <sys/time.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netinet/in_systm.h>
#include <netinet/ip.h>
#include <netinet/ip_icmp.h>
#include <fcntl.h>
#include <netdb.h>

/* This function was taken from the free (as in freedom) ping version */
unsigned short in_cksum(unsigned short *addr, int len)
{
	int             nleft = len;
	int             sum = 0;
	unsigned short  *w = addr;
	unsigned short  answer = 0;

	while(nleft > 1) {
		sum += *w++;
		nleft -= 2;
	}

	if(nleft == 1) {
		*(unsigned char *)(&answer) = *(unsigned char *)w ;
		sum += answer;
	}

	sum = (sum >> 16) + (sum & 0xffff);
	sum += (sum >> 16);
	answer = ~sum;

	return answer;
}

int icmp_send(int sockfd, char *sbuf, struct sockaddr *sin, socklen_t sinlen) {
	char    *data = NULL;
	struct  icmp *header = NULL;
	int     datalen = 0;
 
	datalen = sizeof(struct icmp) + strlen(sbuf);
	data = calloc(datalen+1, sizeof(char));
	header = (struct icmp *)data;

	memcpy(data+sizeof(struct icmp), sbuf, strlen(sbuf)+1);
	*(data+sizeof(struct icmp)+strlen(sbuf)) = '\0';

	header->icmp_type  = 8;
	header->icmp_code  = 0;
	header->icmp_id    = 1000;
	header->icmp_seq   = 0;
	header->icmp_cksum = in_cksum((u_short *)data, datalen);

	/* To see the content of the datagram, you can uncomment the code below */
#if 0
	{
		int fd=0;
		fd = open("/root/packet.txt", O_WRONLY|O_CREAT|O_TRUNC);
		write(fd, data, datalen);
		close(fd);
	}
#endif

	if(sendto(sockfd, data, datalen, 0, sin, sinlen) < 0) {
		perror("sendto: ");
		free(data);
		return -1;
	}
	free(data);

	return 0;
}

int main(int argc, char *argv[])
{
	int     sockfd;
	struct  sockaddr_in sin;
	struct  hostent *host;

	if (argc != 3) {
		fprintf(stderr, "usage: %s <IP> <MESSAGE>\n", argv[0]);
		return 1;
	}

	if((host = gethostbyname(argv[1])) == NULL) {
		perror("gethostbyname: ");
		exit(-1);
	}

	sin.sin_family = AF_INET;
	sin.sin_addr = *((struct in_addr *)host->h_addr);
	memset(&(sin.sin_zero), 0, 8);

	if((sockfd = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP)) == -1) {
		perror("socket: ");
		return 2;
	}

	if(icmp_send(sockfd, argv[2], (struct sockaddr *)&sin, sizeof(sin)) < 0) {
		perror("sending message: ");
		return 3;
	}

	return 0;
}

/* EOF */
