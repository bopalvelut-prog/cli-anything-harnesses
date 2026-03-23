import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('void running')
@cli.command()
def start(): click.echo('void started')
if __name__ == '__main__': cli()
