import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def products(): click.echo('WooCommerce products')
@cli.command()
def orders(): click.echo('WooCommerce orders')
if __name__ == '__main__': cli()
