import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Memcached running on :11211')
@cli.command()
def flush(): click.echo('Cache flushed')
if __name__ == '__main__': cli()
