import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('autowiring running')
@cli.command()
def start(): click.echo('autowiring started')
if __name__ == '__main__': cli()
