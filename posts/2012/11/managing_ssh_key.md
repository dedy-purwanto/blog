title: Managing SSH keys
date: 17/11/2012
tags: komputer

All this time, I've been managing my own SSH keys pretty badly, at least that's how I see it. I have different SSH key for different machine, some with passphrase, others without. 

Whether this is good or not, I believe it remains debatable. Having different SSH keys per machine will make you somehow safe in terms of not having to pass around your private key and storing it in place like Dropbox, you also don't really have to set a passphrase since the possibility of somebody remotely steal your private keys is highly unlikely. But in many ways I think it's inconvenient, in my case, I have to add those new keys to places like Github and Bitbucket everytime I generate them. They will stack up together in time, say in six months, I can't really remember which keys I'm still using, some might be dead already, Especially if you work on sandboxes like Vagrant & VirtualBox for development.

Well, today I decided to remove all those keys, generate a new _global_ SSH key, set a very strong passphrase, and store it in my cloud storage (hint: it's not dropbox). It's really not that complex, the additional part is just putting it in a cloud storage, hell, you can even put it in a password-protected archive if you're super paranoid.

One thing I learned was that you can freely change the user and hostname in your public key in case you don't like it, or in case the host name is too specific / ugly.

But there are risks, for example, if I can't access my cloud storage, or if somebody else have access to it. In that case, there are few things I can do:

* Put a very strong passphrase on the private key, if they have access to your private key, nothing they can do with it.
* Set a very strong password, and multiple-level authentication system on the cloud storage if provided.
* Put the SSH public and private keys in a password-protected archive.
* If shit already happened, delete the public key immediately from places like code hostings, and then delete it from servers since they might not be so popular to get noticed compared to Github, for example.

So from today onwards, there shouldn't be any problem with managing SSH keys, or I can safely say I don't have to do it anymore. 

_Update: When using shared private key like this, you'll have to run `ssh-add` after you add the private key in a another machine, if you've set a passphrase, it will ask you for it, enter it and you should be good to go_
