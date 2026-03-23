import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sake running')
@cli.command()
def start(): click.echo('sake started')
if __name__ == '__main__': cli()
