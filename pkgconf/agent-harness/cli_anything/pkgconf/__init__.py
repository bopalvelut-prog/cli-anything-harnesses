import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pkgconf running')
@cli.command()
def start(): click.echo('pkgconf started')
if __name__ == '__main__': cli()
