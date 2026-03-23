import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('decline running')
@cli.command()
def start(): click.echo('decline started')
if __name__ == '__main__': cli()
