import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('deadlock running')
@cli.command()
def start(): click.echo('deadlock started')
if __name__ == '__main__': cli()
