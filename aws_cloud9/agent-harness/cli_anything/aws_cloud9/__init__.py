import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aws_cloud9 running')
@cli.command()
def start(): click.echo('aws_cloud9 started')
if __name__ == '__main__': cli()
