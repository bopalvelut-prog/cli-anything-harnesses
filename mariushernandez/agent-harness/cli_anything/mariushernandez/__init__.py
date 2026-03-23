import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mariushernandez running')
@cli.command()
def start(): click.echo('mariushernandez started')
if __name__ == '__main__': cli()
