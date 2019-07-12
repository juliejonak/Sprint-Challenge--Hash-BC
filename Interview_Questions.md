1. What is a blockchain and how does it work? 

A blockchain is a linked list of blocks that contain a hash of the previous block's data, and typically stores an index, transactional data, timestamp, and hash of the previous block.

Individuals (or groups) can successfully mine a new block by solving a computationally expensive problem. The complexity of that problem often increases or decreases based on the number of miners, to ensure that blocks are being mined at a consistent rate to store transactions regularly.

The blockchain is stored across a peer to peer network, with each peer acting as a node that verifies each new block that attempts to be added to the chain. This is done via Consensus - by checking that the block's miner is a valid node in the network, the proof is correct, and their hashed reference to the previous block is valid. 

In this way, the blockchain's strength grows with the size of the peer to peer network. This also makes it nearly impossible to brute force hack into a block and change data, because many other nodes' hashed data would not match changes, making the hack invalid. The hacker would need to not only affect one block, but also all subsequent blocks, prior to a new block being mined. Due to the computation and electric expense of mining a single block, this would be nearly impossible.


2. What is an array and how does it work?

An array is a data structure that stores data in a contiguous sequence with a fixed length (size). It is a time efficient data structure for appending and searching, but can have issues when adding data elsewhere into the array and managing memory.

An array allocates a certain amount of space in memory when it is first created, because the memory must be contiguous. If the amount of data exceeds the allocated memory, a new, larger contiguous set of memory space must be found and the old data copied into it.

In a similar vein, adding data into the beginning or middle of an array can be slow because all of the previous data is stored in a row. To insert new data, all the previous data must be shifted one space over.

Data is retrieved using an index, which essentially is the number we multiply the size of the memory storage by, to locate the data to be retrieved (i.e. if we are looking for the second element in the array, we will go to 2 * memory_size_in_bits to find that data). This method works because all of the data is stored in a row.


3. What is a hash table and how does it work?

A hash table is a data structure that uses a hashing function to store data in a dictionary. It uses key value pairs to store and retrieve data.

The data is stored similarly to an array, in that space is allocated when the hash table is created and is in a contiguous block of memory.

The key is converted into an integer using a hash function, and that integer is then converted into an index of the array by a modulo function. This modulo function evaluates the memory capacity allocated to the hash table in relation to the hashed key's integer.

There are instances where two separate keys may result in the same integer -- this is known as a collision. As developers, we have to keep in mind these edge cases and build in ways to handle them, such as storing additional keys at the same index using a linked list, or proactively expanding the capacity of the hashtable when it's at 70-80% capacity, to reduce the liklihood of collisions. Modulo functions aim to evenly distribute indices to avoid collisions.

The hash function used to parse a key into an integer has to follow a few key rules. An input must always have the same consistent output and be unidirectional -- creating the hash is simple, but recreating it backwards (from the integer back to the key) should be nearly impossible.

Hash tables are the logic behind how objects work within several languages, like Python and JavaScript.

Like an array, hashtables are time efficient for looking things up, with an O(1) evaluation. They have the added bonus of being able to look things up by key, rather than index. Being able to use string references to indices can make parsing data much easier.
