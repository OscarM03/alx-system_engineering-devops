<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to <a href="https://intranet.alxswe.com/rltoken/uDfkZ_HQ_YnelvPnhnBOnw" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
    <li>How to read API documentation to find the endpoints you&rsquo;re looking for</li>
    <li>How to use an API with pagination</li>
    <li>How to parse JSON results from an API</li>
    <li>How to make a recursive API call</li>
    <li>How to sort a dictionary by value</li>
</ul>
<h2>Tasks</h2>
<p>&nbsp; &nbsp;</p>
<div>
    <div>&nbsp; &nbsp;<div>
            <h3>&nbsp; &nbsp; &nbsp; 0. How many subs? &nbsp; &nbsp;</h3>&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mandatory &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
        </div>&nbsp;<div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<div>
                <div>
                    <div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
                </div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Score: 0.0% (Checks completed: 0.0%) &nbsp; &nbsp; &nbsp; &nbsp;</div>
            </div>&nbsp; &nbsp; &nbsp; &nbsp;<p>Write a function that queries the <a href="https://intranet.alxswe.com/rltoken/b-4nD6hwEeNYTwYl5yWNwA" title="Reddit API" target="_blank">Reddit API</a> and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.</p>
            <p>Hint: No authentication is necessary for most features of the Reddit API. If you&rsquo;re getting errors related to Too Many Requests, ensure you&rsquo;re setting a custom User-Agent.</p>
            <p>Requirements:</p>
            <ul>
                <li>Prototype: <code>def number_of_subscribers(subreddit)</code></li>
                <li>If not a valid subreddit, return 0.</li>
                <li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.</li>
            </ul>
            <pre><code>wintermancer@lapbox ~/reddit_api/project $ cat 0-main.py
#!/usr/bin/python3
&quot;&quot;&quot;
0-main
&quot;&quot;&quot;
import sys

if __name__ == &apos;__main__&apos;:
    number_of_subscribers = __import__(&apos;0-subs&apos;).number_of_subscribers
    if len(sys.argv) &lt; 2:
        print(&quot;Please pass an argument for the subreddit to search.&quot;)
    else:
        print(&quot;{:d}&quot;.format(number_of_subscribers(sys.argv[1])))
wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py programming
756024
wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py this_is_a_fake_subreddit
0
</code></pre>
        </div>&nbsp;<div>
            <div>
                <p><strong>Repo:</strong></p>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<ul>
                    <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>Directory: <code>0x16-api_advanced</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>File: <code>0-subs.py</code></li>
                </ul>
            </div>
        </div>&nbsp; &nbsp;<div>
            <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
        </div>
    </div>
</div>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p>
<div>
    <div>
        <div>
            <div>
                <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
            </div>
        </div>
    </div>
</div>
<p>&nbsp; &nbsp;&nbsp;</p>
<div>
    <div>&nbsp; &nbsp;<div>
            <h3>&nbsp; &nbsp; &nbsp; 1. Top Ten &nbsp; &nbsp;</h3>&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mandatory &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
        </div>&nbsp;<div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<div>
                <div>
                    <div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
                </div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Score: 0.0% (Checks completed: 0.0%) &nbsp; &nbsp; &nbsp; &nbsp;</div>
            </div>&nbsp; &nbsp; &nbsp; &nbsp;<p>Write a function that queries the <a href="https://intranet.alxswe.com/rltoken/b-4nD6hwEeNYTwYl5yWNwA" title="Reddit API" target="_blank">Reddit API</a> and prints the titles of the first 10 hot posts listed for a given subreddit.</p>
            <p>Requirements:</p>
            <ul>
                <li>Prototype: <code>def top_ten(subreddit)</code></li>
                <li>If not a valid subreddit, print None.</li>
                <li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.</li>
            </ul>
            <pre><code>wintermancer@lapbox ~/reddit_api/project $ cat 1-main.py
#!/usr/bin/python3
&quot;&quot;&quot;
1-main
&quot;&quot;&quot;
import sys

if __name__ == &apos;__main__&apos;:
    top_ten = __import__(&apos;1-top_ten&apos;).top_ten
    if len(sys.argv) &lt; 2:
        print(&quot;Please pass an argument for the subreddit to search.&quot;)
    else:
        top_ten(sys.argv[1])
wintermancer@lapbox ~/reddit_api/project $ python3 1-main.py programming
Firebase founder&apos;s response to last week&apos;s &quot;Firebase Costs increased by 7000%!&quot;
How a 64k intro is made
HTTPS on Stack Overflow: The End of a Long Road
Spend effort on your Git commits
It&apos;s a few years old, but I just discovered this incredibly impressive video of researchers reconstructing sounds from video information alone
From the D Blog: Introspection, Introspection Everywhere
Do MVC like it&rsquo;s 1979
GitHub is moving to GraphQL for v4 of their API (v3 was a REST API)
Google Bug Bounty - The 5k Error Page
PyCon 2017 Talk Videos
wintermancer@lapbox ~/reddit_api/project $ python3 1-main.py this_is_a_fake_subreddit
None
wintermancer@lapbox ~/reddit_api/project $ 
</code></pre>
        </div>&nbsp;<div>
            <div>
                <p><strong>Repo:</strong></p>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<ul>
                    <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>Directory: <code>0x16-api_advanced</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>File: <code>1-top_ten.py</code></li>
                </ul>
            </div>
        </div>&nbsp; &nbsp;<div>
            <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
        </div>
    </div>
</div>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p>
<div>
    <div>
        <div>
            <div>
                <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
            </div>
        </div>
    </div>
</div>
<p>&nbsp; &nbsp;&nbsp;</p>
<div>
    <div>&nbsp; &nbsp;<div>
            <h3>&nbsp; &nbsp; &nbsp; 2. Recurse it! &nbsp; &nbsp;</h3>&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mandatory &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
        </div>&nbsp;<div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<div>
                <div>
                    <div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
                </div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Score: 0.0% (Checks completed: 0.0%) &nbsp; &nbsp; &nbsp; &nbsp;</div>
            </div>&nbsp; &nbsp; &nbsp; &nbsp;<p>Write a <em>recursive function</em> that queries the <a href="https://intranet.alxswe.com/rltoken/b-4nD6hwEeNYTwYl5yWNwA" title="Reddit API" target="_blank">Reddit API</a> and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.</p>
            <p>Hint: The Reddit API uses pagination for separating pages of responses.</p>
            <p>Requirements:</p>
            <ul>
                <li>Prototype: <code>def recurse(subreddit, hot_list=[])</code></li>
                <li>Note: You may change the prototype, but it must be able to be called with just a subreddit supplied. AKA you can add a counter, but it must work without supplying a starting value in the main.</li>
                <li>If not a valid subreddit, return None.</li>
                <li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.</li>
            </ul>
            <p>Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop but the point is to use a recursive function. :)</p>
            <pre><code>wintermancer@lapbox ~/reddit_api/project $ cat 2-main.py
#!/usr/bin/python3
&quot;&quot;&quot;
2-main
&quot;&quot;&quot;
import sys

if __name__ == &apos;__main__&apos;:
    recurse = __import__(&apos;2-recurse&apos;).recurse
    if len(sys.argv) &lt; 2:
        print(&quot;Please pass an argument for the subreddit to search.&quot;)
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print(&quot;None&quot;)
wintermancer@lapbox ~/reddit_api/project $ python3 2-main.py programming
932
wintermancer@lapbox ~/reddit_api/project $ python3 2-main.py this_is_a_fake_subreddit
None
</code></pre>
        </div>&nbsp;<div>
            <div>
                <p><strong>Repo:</strong></p>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<ul>
                    <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>Directory: <code>0x16-api_advanced</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>File: <code>2-recurse.py</code></li>
                </ul>
            </div>
        </div>&nbsp; &nbsp;<div>
            <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
        </div>
    </div>
</div>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p>
<div>
    <div>
        <div>
            <div>
                <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
            </div>
        </div>
    </div>
</div>
<p>&nbsp; &nbsp;</p>
<p>&nbsp; &nbsp; &nbsp;&nbsp;</p>
<form method="post" action="/projects/314/unlock_optionals"><br></form>
<article>
    <div>
        <div>
            <div>
                <div>
                    <form method="post" action="/projects/314/unlock_optionals"><br></form>&nbsp; &nbsp;&nbsp;<p><br></p>
                </div>
            </div>
        </div>
    </div>
</article>
<p>&nbsp; &nbsp; &nbsp;</p>
<div><br></div>