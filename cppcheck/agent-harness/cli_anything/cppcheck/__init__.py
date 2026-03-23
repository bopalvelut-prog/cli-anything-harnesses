import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cppcheck running')
@cli.command()
def start(): click.echo('cppcheck started')
if __name__ == '__main__': cli()
