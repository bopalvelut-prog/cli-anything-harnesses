import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cherokee running')
@cli.command()
def start(): click.echo('cherokee started')
if __name__ == '__main__': cli()
