import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wrong running')
@cli.command()
def start(): click.echo('wrong started')
if __name__ == '__main__': cli()
