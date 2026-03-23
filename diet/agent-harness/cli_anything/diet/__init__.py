import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('diet running')
@cli.command()
def start(): click.echo('diet started')
if __name__ == '__main__': cli()
