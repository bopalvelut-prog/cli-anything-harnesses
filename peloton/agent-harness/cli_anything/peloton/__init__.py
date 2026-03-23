import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('peloton running')
@cli.command()
def start(): click.echo('peloton started')
if __name__ == '__main__': cli()
