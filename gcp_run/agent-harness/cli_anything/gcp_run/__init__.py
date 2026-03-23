import click
@click.group()
def cli(): pass
@cli.command()
def deploy(): click.echo('Cloud Run deploy')
@cli.command()
def services(): click.echo('Cloud Run services')
if __name__ == '__main__': cli()
