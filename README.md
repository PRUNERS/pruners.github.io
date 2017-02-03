<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#org931bcd2">1. Description</a></li>
<li><a href="#orgb7d0bed">2. Prerequisites</a>
<ul>
<li><a href="#orgc2928e2">2.1. Install on Mac OS</a></li>
</ul>
</li>
<li><a href="#org90da02f">3. How to generate the site</a></li>
</ul>
</div>
</div>


<a id="org931bcd2"></a>

# Description

The PRUNERS Website is developed using [HUGO](http://gohugo.io), [Bootstrap 3](http://getbootstrap.com) and HTML5.

It is a static website, all you need to do is fill up a Markdown page
and re-generate the site.


<a id="orgb7d0bed"></a>

# Prerequisites

Only prerequisite is the HUGO engine.


<a id="orgc2928e2"></a>

## Install on Mac OS

brew update && brew install hugo

For details go [<http://gohugo.io/#action][here>]].


<a id="org90da02f"></a>

# How to generate the site

-   Once you clone the repository, you need to checkout the branch
    *gh-pages*.
-   Modify your Markdown page.
-   From the root folder of the web site run:

        hugo --verbose && hugo --verbose serve

    This will generate the site and run a local server to verify that
    the new edits are correct.
-   Once the site is ready to be published, from the *gh-pages* branch,
    run:

        ./scripts/publish_tomaster.sh

    This command will commit and push the modification on the *master*
    branch which is the branch that GitHub uses to publish the content
    of the website.
