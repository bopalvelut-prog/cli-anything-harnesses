import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('algernon running')
@cli.command()
def start(): click.echo('algernon started')
if __name__ == '__main__': cli()
