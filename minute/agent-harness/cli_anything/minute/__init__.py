import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('minute running')
@cli.command()
def start(): click.echo('minute started')
if __name__ == '__main__': cli()
