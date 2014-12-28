$(document).ready(function() {
	var nadigan = "http://104.236.66.27:9000/home_data/";

	//section 1.1
	var section_1_1 = _.template('<article class="entry style-grid style-hero hero-md-largest type-post col-md-8 col-lg-12 colheight-sm-1 colheight-md-2 colheight-lg-2 colheight-xl-2"> <div class="ribbon ribbon-pulled ribbon-small ribbon-highlight"><a href="blog.html"><%- section %></a></div><header class="entry-header"><h3 class="entry-title"><a href="single.html"><%- title %></a></h3></header><figure class="entry-thumbnail"><a href="single.html" class="overlay overlay-primary"></a><img src=/static/img/<%- image %> data-src=/static/img/<%- image %> width="680" height="452" alt=""><noscript><img src="../uploads/680x452_2.jpg" alt=""></noscript></figure></article>');
	
	//section 1.2
	var section_1_2 = _.template('<article class="entry style-grid style-hero type-post col-md-4 col-lg-6 colheight-sm-1"> <div class="ribbon ribbon-pulled ribbon-small ribbon-highlight"><a href="blog.html"><%- section %></a></div><header class="entry-header"><h3 class="entry-title"><a href="single.html"><%- title %></a></h3></header><figure class="entry-thumbnail"><a href="single.html" class="overlay overlay-primary"></a><img src=/static/img/<%- image %> data-src=/static/img/<%- image %> width="680" height="452" alt=""><noscript><img src="../uploads/680x452_2.jpg" alt=""></noscript></figure></article>');

	//section 1.3
	var section_1_3 = _.template('<article class="entry style-grid style-hero type-post col-md-4 col-lg-6 colheight-sm-1"> <div class="ribbon ribbon-pulled ribbon-small ribbon-highlight"><a href="blog.html"><%- section %></a></div><header class="entry-header"><h3 class="entry-title"><a href="single.html"><%- title %></a></h3></header><figure class="entry-thumbnail"><a href="single.html" class="overlay overlay-primary"></a><img src=/static/img/<%- image %> data-src=/static/img/<%- image %> width="680" height="452" alt=""><noscript><img src="../uploads/680x452_2.jpg" alt=""></noscript></figure></article>');

	//section 1.4
        var section_1_4 = _.template('<article class="entry style-grid style-hero hero-lg-larger type-post col-md-4 col-lg-6 colheight-sm-1 colheight-lg-2"> <div class="ribbon ribbon-pulled ribbon-small ribbon-highlight"><a href="blog.html"><%- section %></a></div><header class="entry-header"><h3 class="entry-title"><a href="single.html"><%- title %></a></h3></header><figure class="entry-thumbnail"><a href="single.html" class="overlay overlay-primary"></a><img src=/static/img/<%- image %> data-src=/static/img/<%- image %> width="680" height="452" alt=""><noscript><img src="../uploads/680x452_2.jpg" alt=""></noscript></figure></article>');

	//section 1.5
        var section_1_5 = _.template('<article class="entry style-grid style-hero type-post col-md-6 col-lg-6 colheight-sm-1"> <div class="ribbon ribbon-pulled ribbon-small ribbon-highlight"><a href="blog.html"><%- section %></a></div><header class="entry-header"><h3 class="entry-title"><a href="single.html"><%- title %></a></h3></header><figure class="entry-thumbnail"><a href="single.html" class="overlay overlay-primary"></a><img src=/static/img/<%- image %> data-src=/static/img/<%- image %> width="680" height="452" alt=""><noscript><img src="../uploads/680x452_2.jpg" alt=""></noscript></figure></article>');

	//reviews_section
	var review_1_1 = _.template('<article class="entry style-large type-post"><figure class="entry-thumbnail hidden-xs"><a href="single.html"><img src="../img/placeholder.gif" data-src="../uploads/680x452_4.jpg" data-src-retina="../uploads/1024x680_4.jpg" width="680" height="452" alt=""><noscript><img src="../uploads/680x452_4.jpg" alt=""></noscript></a></figure><header class="entry-header"><h3 class="entry-title"><a href="single.html" rel="bookmark"><%- title %></a></h3></header><p><%- hits %></p></article>')

	//reviews_section
	var review_1_2 = _.template('<article class="type-post style-media-list media col-sm-6 col-md-12"><img src="../img/placeholder.gif" data-src="../uploads/80x80_1.jpg" data-src-retina="../uploads/160x160_2.jpg" width="80" height="80" class="media-object pull-left" alt=""><noscript><img src="../uploads/80x80_1.jpg" alt=""></noscript><div class="media-body"><h3  class="entry-title"><a href="single.html" rel="bookmark"><%- title %></a></h3></div></article>')

	//nadigan special
	var nadigan_special = _.template('<article class="type-post style-media-list style-review-list media col-sm-6 col-md-12"><img src="../img/placeholder.gif" data-src="../uploads/80x80_6.jpg" data-src-retina="../uploads/160x160_2.jpg" width="80" height="80" class="media-object pull-left" alt=""><noscript><img src="../uploads/80x80_6.jpg" alt=""></noscript><div class="media-body"><h3  class="entry-title"><a href="single-full.html" rel="bookmark">Nadigan Spl</a></h3><p class="small"><%- title %></p></div></article>')

	//new_articles
	var news_articles = _.template('<article class="entry type-post style-thumbnail-text col-sm-6 col-md-2 colheight-sm-1"><div class="entry-meta"><span class="category"><a href="blog.html"><%- section %></a></span></div><h3 class="entry-title"><a href="single.html" rel="bookmark"><%- title %></a></h3></article>')

	//gallery
	var gallery = _.template('<article class="entry style-grid type-post col-md-6 col-lg-3 colheight-sm-1"><header class="entry-header"><h3 class="entry-title"><a href=/gallery/<%- id %>><%- title %></a> </h3></header><figure class="entry-thumbnail"><a href=/gallery/<%- id %> class="overlay overlay-primary"></a><img src="../img/placeholder.gif" data-src="../uploads/480x280_1.jpg" data-src-retina="../uploads/720x420_1.jpg" width="480" height="280" alt=""><noscript><img src="../uploads/480x280_1.jpg" alt=""></noscript></figure></article>')

    $.getJSON(nadigan, {
            format: "json"
        }).done(function(data) {
		$("#topsection1").append(section_1_1(data.topsection[0]));
		
		$.each(data.topsection.slice(1, 3),  function(i, item) {
			$("#topsection1").append(section_1_2(item));
		});

		$("#topsection2").append(section_1_4(data.topsection[4]));

		$.each(data.topsection.slice(5, 7),  function(i, item) {
                        $("#topsection2").append(section_1_3(item));
                });

		$.each(data.topsection.slice(7, 9),  function(i, item) {
                        $("#topsection2").append(section_1_5(item));
                });

		$.each(data.reviews.slice(0, 3),  function(i, item) {
                        $("#reviews1").append(review_1_1(item));
                });

		$.each(data.reviews.slice(0, 10),  function(i, item) {
			$("#reviews2").append(review_1_2(item));
		});

		$.each(data.nadigan_spl.slice(0, 6),  function(i, item) {
			$("#nadiganspl").append(nadigan_special(item));
		});

		$.each(data.news_articles.slice(0, 6),  function(i, item) {
                        $("#newsarticles").append(news_articles(item));
                });

		$.each(data.gallery.personality.slice(0,4), function(i, item) {
			$("#personality").append(gallery(item));
		});

		$.each(data.gallery.movie.slice(0,4), function(i, item) {
                        $("#movie").append(gallery(item));
                });



	});
});
