import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('boxfuse running')
@cli.command()
def start(): click.echo('boxfuse started')
if __name__ == '__main__': cli()
