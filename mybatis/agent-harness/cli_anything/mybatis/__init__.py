import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mybatis running')
@cli.command()
def start(): click.echo('mybatis started')
if __name__ == '__main__': cli()
