import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lead running')
@cli.command()
def start(): click.echo('lead started')
if __name__ == '__main__': cli()
