import click
@click.group()
def cli(): pass
@cli.command()
def zones(): click.echo('DNS zones')
@cli.command()
def records(): click.echo('DNS records')
if __name__ == '__main__': cli()
