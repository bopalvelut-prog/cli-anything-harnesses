import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def products(): click.echo('PrestaShop products')
@cli.command()
def orders(): click.echo('PrestaShop orders')
if __name__ == '__main__': cli()
