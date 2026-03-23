import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shock running')
@cli.command()
def start(): click.echo('shock started')
if __name__ == '__main__': cli()
