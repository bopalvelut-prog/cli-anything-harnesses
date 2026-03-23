import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('participant running')
@cli.command()
def start(): click.echo('participant started')
if __name__ == '__main__': cli()
