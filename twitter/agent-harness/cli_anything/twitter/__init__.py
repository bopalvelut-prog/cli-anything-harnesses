import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('twitter running')
@cli.command()
def start(): click.echo('twitter started')
if __name__ == '__main__': cli()
