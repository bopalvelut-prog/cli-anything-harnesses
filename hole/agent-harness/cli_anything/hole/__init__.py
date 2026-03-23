import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hole running')
@cli.command()
def start(): click.echo('hole started')
if __name__ == '__main__': cli()
