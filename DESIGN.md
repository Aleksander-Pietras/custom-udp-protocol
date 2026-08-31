## Design

### Objective

The finished protocol will
* Establish a connection by listening on a port, performing a handshake and starting a session
* Handle the session using a session ID to allow ports to change
* Handle encryption and decryption of each packet
* Hanlde requesting missing packets within a set timeout window
* Handle checksum to catch corrupted data
* Handle duplicate packets

### Plan
- [ ] Create a simple localhost connection
- [ ] Create a function for setting up a header
- [ ] Create a function for ordering packets
- [ ] Add a checksum
- [ ] Add simple packet encryption
- [ ] Add a session ID in headder (to be used later)
- [ ] Unit test: connection, header generation, ordering, checksum, encryption

- [ ] Create a function for requesting missing/corrupt packets
- [ ] Unit test

- [ ] Create a function for handling duplicates
- [ ] Unit test

- [ ] Change connection to run across a stable home LAN between two fixed machines
- [ ] Test full system

- [ ] Create a function to handle sessions
- [ ] Unit test

- [ ] Create a function to handle handshakes and authentication
- [ ] Unit test

- [ ] Change connection to run across Internet between two fixed machines across the country


