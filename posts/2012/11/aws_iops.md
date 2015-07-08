Title: Optimizing I/O cost with provisioned IOPS
Tags: komputer
date: 10/11/2012

Recently I've been watching my monthly AWS bill and notice the I/O cost has been increased in the last few months. Note that at this point I've been receiving something around 220 million I/O request on my EBS volume. Earlier this week, Amazon Singapore did an introductory workshop nearby our office and introduces provisioned IOPS. I didn't really paid any attention to it, but it turned out really handy.

IOPS, or IO per second, is a term coined by AWS to allow some resource in EBS volume in order to serve I/O requests, the more you have it, the more you can serve a request in a second. In AWS, there are two flavors of EBS, standard or provisioned, from the latter you will be able to set how many IOPS you want to have in a month, which is called as IOPS-month. 1 IOPS-month is equal to the number of seconds in a month, which is approximately 27 million second, or 27 million IOPS. When looking at my monthly I/O requests, which was 220 million, I can safely provision my IOPS to 100 IOPS which is something around 270 million IOPS per month, a bit higher and also safer in case of sudden peak.

When using a standard I/O request, you will be charged something around 11 cents per 1 million request, and when using provisioned IOPS, you will be charged 11 cents per 1 IOPS-month, this will approximately save $10 a month for I/O requests. Pricing will depends on region, and provisioned storage will cost more for space, but the end cost is cheaper.

So far, the only way to use this provisioned IOPS is by creating a new instance / launching new EBS volume, I haven't figured any way to switch my EBS volume to use a provisioned IOPS. For more info, see the EBS detail page in AWS (http://aws.amazon.com/ebs/).
