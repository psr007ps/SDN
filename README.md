# SDN
A project based on software defined networking in which following four parts were achieved:


Part A: Hub controller
All traffic arriving on a switch will be forwarded to the controller. The controller then instructs
the switch to forward the packet on all ports except the one it arrived on. This is the default
behavior of the of_tutorial.py controller.
1. Have h1 ping h2 and h1 ping h5. How long did it take to ping? What is the
difference? Which of the hosts and switches observe traffic?
2. Run iperf h1 h2 and iperf h1 h5. What is the throughput? What is the
difference?
3. Run pingall to verify connectivity and dump the output.



Part B: MAC learning controller
All traffic arriving on a switch will be forwarded to the controller. Modify the default controller
so that, for each switch, it learns the mapping between MAC addresses and ports. It then
instructs the switch which port to forward the packet on.
Host
1
Host
4
Switch
1
Switch
2
Switch
3
Host
2
Host
Host 5
3
1. Have h1 ping h2 and h1 ping h5. How long did it take to ping? What is the
difference? Which of the hosts and switches observe traffic? How does this compare to
the hub controller?
2. Run iperf h1 h2 and iperf h1 h5. What is the throughput? What is the
difference? How does this compare to the hub controller?
3. Run pingall to verify connectivity and dump the output.



Part C: MAC learning switch
Now, we will try to make the switch a bit smarter. Modify the controller from Part B so that
when it learns a mapping, it installs a flow rule on the switch to handle future packets. Thus, the
only packets that should arrive at the controller are those that the switch doesn’t have a flow
entry for.
1. Have h1 ping h2 and h1 ping h5. How long did it take to ping? What is the
difference? Which of the hosts and switches observe traffic? How does this compare to
Part A, and why?
2. Run iperf h1 h2 and iperf h1 h5. What is the throughput? What is the
difference? How does this compare to Part A?
3. Run pingall to verify connectivity and dump the output.
4. Dump the output of the flow rules using ovs-ofctl dump-flows. How many rules
are there, and why?
Bonus: if you used the of.ofp_match.from_packet function to create the flow rule, that
might explain why there are so many rules. Can you think of a way to reduce the number of
rules, and implement this in the controller?



Part D: Simplified IP router
Finally, we will do a bit of layer-3 routing. This is a simplified version of an IP router where we
ignore several aspects such as TTL, checksum, and ARP. Modify the topology so the hosts H1-5
have IP addresses 10.0.0.1, 10.0.0.2, 10.0.0.3, 10.0.1.2, 10.0.1.3 respectively (but are still on the
same subnet, e.g., /16). Install IP-matching rules on switch 2 (hint: use ovs-ofctl and match
on /24). Let switches 1 and 3 stay as MAC learning switches.
1. Have h1 ping h2 and h1 ping h5. How long did it take to ping? What is the difference?
Which of the hosts and switches observe traffic? How does this compare to the previous
controllers?
2. Run iperf h1 h2 and iperf h1 h5. What is the throughput? What is the difference? How
does this compare to the previous controllers?
3. Run pingall to verify connectivity and dump the output.
4. Dump the output of the flow rules using ovs-ofctl dump-flows. How many rules are
there, and why?
5. How does this network compare to your previous controllers? Which is better, and why?
