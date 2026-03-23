import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('credit running')
@cli.command()
def start(): click.echo('credit started')
if __name__ == '__main__': cli()
