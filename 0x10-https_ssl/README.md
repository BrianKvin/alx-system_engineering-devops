1. Background Context
2. What happens when you don’t secure your website traffic?


3. Resources:

   - [DNS](https://intranet.alxswe.com/concepts/12)
   - [Web stack debugging](https://intranet.alxswe.com/concepts/68)
   - [What is HTTPS?](https://www.instantssl.com/http-vs-https)
   - [What are the 2 main elements that SSL is providing](https://www.instantssl.com/http-vs-https)
   - [HAProxy SSL termination on Ubuntu16.04](https://www.sslshopper.com/why-ssl-the-purpose-of-using-ssl-certificates.html)
   - [SSL termination](https://docs.ionos.com/cloud/)
4. Bash function
5. man or help:

   - awk
   - dig
6. Learning Objectives
7. At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

8. General
9. What is HTTPS SSL 2 main roles
10. What is the purpose encrypting traffic
11. What SSL termination means
12. Requirements
13. General
14. Allowed editors: vi, vim, emacs
15. All your files will be interpreted on Ubuntu 16.04 LTS
16. All your files should end with a new line
17. A README.md file, at the root of the folder of the project, is mandatory
18. All your Bash script files must be executable
19. Your Bash script must pass Shellcheck (version 0.3.7) without any error
20. The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
21. The second line of all your Bash scripts should be a comment explaining what is the script doing
22. Quiz questions
23. Great! You've completed the quiz successfully! Keep going! (Show quiz)
24. Your servers
25. Name	Username	IP	State	
26. 114338-web-01	ubuntu	3.86.7.131	running	
27. 114338-web-02	ubuntu	100.26.243.119	running	
28. 114338-lb-01	ubuntu	54.236.46.252	running	
29. Tasks
0. World wide web
mandatory
1. Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

2. Requirements:

3. Add the subdomain www to your domain, point it to your lb-01 IP (your domain name might be configured with default subdomains, feel free to remove them)
4. Add the subdomain lb-01 to your domain, point it to your lb-01 IP
5. Add the subdomain web-01 to your domain, point it to your web-01 IP
6. Add the subdomain web-02 to your domain, point it to your web-02 IP
7. Your Bash script must accept 2 arguments:
8. domain:
9. type: string
10. what: domain name to audit
11. mandatory: yes
12. subdomain:
13. type: string
14. what: specific subdomain to audit
15. mandatory: no
16. Output: The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]
17. When only the parameter domain is provided, display information for its subdomains www, lb-01, web-01 and web-02 - in this specific order
18. When passing domain and subdomain parameters, display information for the specified subdomain
18. Ignore shellcheck case SC2086
19. Must use:
awk
at least one Bash function
You do not need to handle edge cases such as:
Empty parameters
Nonexistent domain names
Nonexistent subdomains
20. Example:

sylvain@ubuntu$ dig www.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
www.holberton.online.   87  IN  A   54.210.47.110
sylvain@ubuntu$ dig lb-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
lb-01.holberton.online. 101 IN  A   54.210.47.110
sylvain@ubuntu$ dig web-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-01.holberton.online. 212    IN  A   34.198.248.145
sylvain@ubuntu$ dig web-02.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-02.holberton.online. 298    IN  A   54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online
The subdomain www is a A record and points to 54.210.47.110
The subdomain lb-01 is a A record and points to 54.210.47.110
The subdomain web-01 is a A record and points to 34.198.248.145
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online web-02
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
   
1. HAproxy SSL termination
mandatory
2. “Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.

3. Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www..

Requirements:

HAproxy must be listening on port TCP 443
HAproxy must be accepting SSL traffic
HAproxy must serve encrypted traffic that will return the / of your web server
When querying the root of your domain name, the page returned must contain Holberton School
Share your HAproxy config as an answer file (/etc/haproxy/haproxy.cfg)
The file 1-haproxy_ssl_termination must be your HAproxy configuration file

Make sure to install HAproxy 1.5 or higher, SSL termination is not available before v1.5.

Example:

sylvain@ubuntu$ curl -sI https://www.holberton.online
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 01:52:04 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes
sylvain@ubuntu$
sylvain@ubuntu$ curl https://www.holberton.online
Holberton School for the win!
sylvain@ubuntu$
   
2. No loophole in your website traffic
#advanced
A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS.

Requirements:

This should be transparent to the user
HAproxy should return a 301
HAproxy should redirect HTTP traffic to HTTPS
Share your HAproxy config as an answer file (/etc/haproxy/haproxy.cfg)
The file 100-redirect_http_to_https must be your HAproxy configuration file

Example:

sylvain@ubuntu$ curl -sIL http://www.holberton.online
HTTP/1.1 301 Moved Permanently
Content-length: 0
Location: https://www.holberton.online/
Connection: close

HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 02:19:18 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes

sylvain@ubuntu$
