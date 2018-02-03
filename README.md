# Download-With-TCP
 TCP/IP – A Brief Explanation

The Internet works by using a protocol called TCP/IP, or Transmission Control Protocol/Internet Protocol. TCP/IP is the underlying communication language of the Internet. In base terms, TCP/IP allows one computer to talk to another computer via the Internet through compiling packets of data and sending them to right location.

For those who don’t know, a packet, sometimes more formally referred to as a network packet, is a unit of data transmitted from one location to another. Much like the atom is the smallest unit of a cell, a packet is the smallest unit of transmitted information over the Internet.
Defining TCP

As indicated in the name, there are two layers to TCP/IP. The top layer, TCP, is responsible for taking large amounts of data, compiling it into packets and sending them on their way to be received by a fellow TCP layer, which turns the packets into useful information/data.
Defining IP

The bottom layer, IP, is the locational aspect of the pair allowing the packets of information to be sent and received to the correct location. If you think about IP in terms of a map, the IP layer serves as the packet GPS to find the correct destination. Much like a car driving on a highway, each packet passes through a gateway computer (signs on the road), which serve to forward the packets to the right destination.

    In summary, TCP is the data. IP is the Internet location GPS.

That is how the Internet works on the surface. Let’s take a look below the surface at the abstraction layers of the Internet.
The Four Abstraction Layers Embedded in TCP/IP

The four abstraction layers are the link layer (lowest layer), the Internet layer, the transport layer and the application layer (top layer).

They work in the following fashion:

    The Link Layer is the physical network equipment used to interconnect nodes and servers.
    The Internet Layer connects hosts to one another across networks.
    The Transport Layer resolves all host-to-host communication.
    The Application Layer is utilized to ensure communication between applications on a network.

In English, the four abstraction layers embedded in TCP/IP allow packets of data, application programs and physical network equipment to communicate with one another over the Internet to ensure packets are sent intact and to the correct location.

The Four Abstraction Layers Embedded in TCP/IP

Now that you know the base definition of TCP/IP and how the Internet works, we need to discuss why all of this matters.
The Internet is About Communication and Access

The common joke about the Internet is it is a series of tubes where data is sent and received at different locations. The analogy isn’t bad. However, it isn’t complete.

The Internet is more like a series of tubes with various connection points, various transmission points, various send/receive points, various working speeds and a governing body watching over the entire process.

To understand why TCP/IP is needed, here’s a quick example.

I live in Gainesville, Florida. However, because I once lived in Auckland, New Zealand, for an extended period of time, I enjoy checking the local New Zealand news on a weekly basis.

To do this, I read The New Zealand Herald. To do this, I visit www.nzhearald.co.nz. As you might have guessed from the URL, The New Zealand Herald is digitally based in New Zealand (i.e. the other side of the world from Gainesville).
The Amount of Hops For Packets to Be Transmitted

For the connection to be made from my computer located in Gainesville to a server hosting The New Zealand Herald based in New Zealand, packets of data have to be sent to multiple data centers through multiple gateways and through multiple verification channels to ensure my request finds the right destination.

The common Internet parlance for this is finding out how many hops it takes for one packet of information to be sent to another location.

Running a trace route can show you the amount of hops along the way. If you are wondering, there are 17 hops between my location in Gainesville and the server hosting the The New Zealand Herald website.

TCP/IP is needed to ensure that information reaches its intended destination. Without TCP/IP, packets of information would never arrive where they need to be and the Internet wouldn’t be the pool of useful information that we know it to be today.
