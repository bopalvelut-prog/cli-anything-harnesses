import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('work running')
@cli.command()
def start(): click.echo('work started')
if __name__ == '__main__': cli()
