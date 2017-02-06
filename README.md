<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgc1505fa">1. Description</a></li>
<li><a href="#org4aaf1c1">2. Prerequisites</a>
<ul>
<li><a href="#org0ba7490">2.1. Install on Mac OS</a></li>
</ul>
</li>
<li><a href="#org1cfa3fd">3. How to generate the site</a></li>
</ul>
</div>
</div>


<a id="orgc1505fa"></a>

# Description

The PRUNERS Website is developed using [HUGO](http://gohugo.io), [Bootstrap 3](http://getbootstrap.com) and HTML5.

It is a static website, all you need to do is fill up a Markdown page
and re-generate the site.


<a id="org4aaf1c1"></a>

# Prerequisites

Only prerequisite is the HUGO engine.


<a id="org0ba7490"></a>

## Install on Mac OS

    brew update && brew install hugo

For details go [here](http://gohugo.io/#action).


<a id="org1cfa3fd"></a>

# How to generate the site

-   Once you cloned the repository, you need to checkout the branch
    *gh-pages*.
-   Modify your Markdown pages.
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
