import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('circleci running')
@cli.command()
def start(): click.echo('circleci started')
if __name__ == '__main__': cli()
