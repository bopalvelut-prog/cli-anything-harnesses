import click
@click.group()
def cli(): pass
@cli.command()
def invoke(): click.echo('Lambda invoke')
@cli.command()
def list(): click.echo('Lambda list')
if __name__ == '__main__': cli()
