# Massive-Subdomain-Enumerator

<p>This tool uses a combination of dictionary-based wordlists (brute-force) and DNS resolution checks to verify the existence of subdomains.</p>

![Massive-Subdomain-Enumerator Jenderal92](https://github.com/user-attachments/assets/7f1e767e-4b93-4506-ba2c-9b58f582e99f)


## Features

<ul>
    <li><strong>Wordlist Processing:</strong> Capable of handling large wordlists efficiently.</li>
    <li><strong>Multi-threading:</strong> Boosts search speed by using multiple threads.</li>
    <li><strong>DNS Validation:</strong> Displays only valid and active subdomains.</li>
    <li><strong>Output to File:</strong> Saves the enumeration results to a file for further analysis.</li>
</ul>

## How to Use

<ol>
    <li>
        <p><strong>Download and Install Python</strong></p>
        <p>Ensure Python 2.7 is installed on your system. You can download it from the official Python website: 
        <a href="https://www.python.org" target="_blank">https://www.python.org</a>.</p>
    </li>
    <li>
        <p><strong>Prepare the Wordlist</strong></p>
        <p>Create a text file containing the list of subdomains you want to test. Example content for <code>wordlist.txt</code>:</p>
        <pre>
www
mail
ftp
admin
dev
        </pre>    
    </li>
    <li>
        <p><strong>Run the Script</strong></p>
        <p>Use the following command to execute the script:</p>
        <pre><code>python2 massive_subenum.py -d target.com -w wordlist.txt -t 20 -o results.txt</code></pre>
        <ul>
            <li><strong><code>-d</code>:</strong> Target domain.</li>
            <li><strong><code>-w</code>:</strong> Path to the wordlist.</li>
            <li><strong><code>-t</code>:</strong> Number of threads (optional, default: 10).</li>
            <li><strong><code>-o</code>:</strong> Output file to save the results (optional).</li>
        </ul>
    </li>
</ol>

## Disclaimer !!!

<p>I have written the disclaimer on the cover of Jenderal92. You can check it <a href="https://github.com/Jenderal92">HERE !!!</a></p>
