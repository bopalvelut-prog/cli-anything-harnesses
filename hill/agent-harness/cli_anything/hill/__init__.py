import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hill running')
@cli.command()
def start(): click.echo('hill started')
if __name__ == '__main__': cli()
