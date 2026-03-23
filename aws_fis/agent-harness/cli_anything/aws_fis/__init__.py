import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aws_fis running')
@cli.command()
def start(): click.echo('aws_fis started')
if __name__ == '__main__': cli()
