from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
	"""
        leftHost1 = self.addHost( 'h1', ip = '10.0.0.1' )
	leftHost2 = self.addHost( 'h2', ip = '10.0.0.2' )
	leftHost3 = self.addHost( 'h3', ip = '10.0.0.3' )
        rightHost1 = self.addHost( 'h4', ip = '10.0.1.2' )
	rightHost2 = self.addHost( 'h5', ip = '10.0.1.3' )
	"""
        leftHost1 = self.addHost( 'h1' )
        leftHost2 = self.addHost( 'h2' )
        leftHost3 = self.addHost( 'h3' )
        rightHost1 = self.addHost( 'h4' )
        rightHost2 = self.addHost( 'h5' )
	leftSwitch = self.addSwitch( 's1' )
	centerSwitch = self.addSwitch('s2')
        rightSwitch = self.addSwitch( 's3' )

        # Add links
        self.addLink( leftHost1, leftSwitch )
	self.addLink( leftHost2, leftSwitch )
	self.addLink( leftHost3, leftSwitch )
        self.addLink( leftSwitch, centerSwitch )
	self.addLink( centerSwitch, rightSwitch )
        self.addLink( rightSwitch, rightHost1 )
	self.addLink( rightSwitch, rightHost2 )


topos = { 'mytopo': ( lambda: MyTopo() ) }

