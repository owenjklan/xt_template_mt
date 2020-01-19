# Xtables Match Extension Templates #
This project started life as I began writing my first xtables
match extension. I realised that if I did the bare minimum to
get a functional kernel module and matching extension plugin
for the iptables command line, I could easily template this
work so that it can be easily generated from a Jinja2 template.


## An important note ##
As this my first attempt at extending iptables capabilites via
xtables, I make *no guarantees what-so-ever* regarding correctness
of what's presented here. This project will hopefully evolve to
be more flexible in future. Hopefully the current state of the
project at the time of reading is at least usable to someone.

## A bunch of handy links ##
The following links may be useful while developing xtables
extensions:
- [Writing your own Xtables module](http://www.kerneltravel.net/jiaoliu/Writing_Xtables.pdf) - You will find that key function
prototypes and data structures will have changed, sometimes in
more ways than by name. **xt_template_mt** has obviously been
updated to work with the modern state of affairs (as of January 2020).