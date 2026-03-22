import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def products(): click.echo('BigCommerce products')
@cli.command()
def orders(): click.echo('BigCommerce orders')
if __name__ == '__main__': cli()
