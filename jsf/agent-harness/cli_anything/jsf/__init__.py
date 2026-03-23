import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jsf running')
@cli.command()
def start(): click.echo('jsf started')
if __name__ == '__main__': cli()
