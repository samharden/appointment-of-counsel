<?php
/**
 * The template part for displaying footer section.
 * @package TheFour Lite
 */
?>

</main>

<footer class="footer"  role="contentinfo">
	<div class="container">
		<?php
		$footer_sidebars = array( 'footer', 'footer-2', 'footer-3', 'footer-4' );
		$has_widget      = false;
		foreach ( $footer_sidebars as $footer_sidebar )
		{
			if ( is_active_sidebar( $footer_sidebar ) )
			{
				$has_widget = true;
				break;
			}
		}
		?>
		<?php if ( $has_widget ) : ?>
			<div class="footer-widgets row clearfix">
				<?php foreach ( $footer_sidebars as $footer_sidebar ) : ?>
					<?php if ( is_active_sidebar( $footer_sidebar ) ) : ?>
						<div class="column one-fourth">
							<div class="widgets">
								<?php dynamic_sidebar( $footer_sidebar ); ?>
							</div>
						</div>
					<?php endif; ?>
				<?php endforeach; ?>
			</div>
		<?php endif; ?>

		<div class="credits clearfix">

			
			<div class="left">
				<?php
				printf(
					esc_html__( '%s.', 'info@mycourtcase.org' ),
					sprintf( '<a href="%s">%s</a>', esc_url( 'mailto:info@mycourtcase.org' ), 'Contact Us')
				);
				?>
			</div>
			<div class="right">
				<?php
				printf(
					esc_html__( '%s.', 'data' ),
					sprintf( '<a href="%s">%s</a>', esc_url( 'http://www.mycourtcase.org/open-source-data/' ), 'Open Source Data' )
				);
				?>
			</div>
					
	
<p style="text-align: justify;"><a href="http://creativecommons.org/licenses/by-nc-nd/4.0/" rel="license"><img class="aligncenter" style="border-width: 0;" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" alt="Creative Commons License" /></a>
This work is licensed under a <a href="http://creativecommons.org/licenses/by-nc-nd/4.0/" rel="license">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.</p>
			


		</div>
	</div>
</footer><!-- .footer -->

</div><!-- .wrapper -->

<?php wp_footer(); ?>

<nav class="mobile-navigation" role="navigation">
	<?php
	wp_nav_menu( array(
		'container_class' => 'mobile-menu',
		'menu_class'      => 'mobile-menu clearfix',
		'theme_location'  => 'primary',
		'items_wrap'      => '<ul>%3$s</ul>',
	) );
	?>
</nav>

</body>
</html>