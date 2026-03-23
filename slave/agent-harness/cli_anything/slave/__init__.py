import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('slave running')
@cli.command()
def start(): click.echo('slave started')
if __name__ == '__main__': cli()
